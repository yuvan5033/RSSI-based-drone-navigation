import numpy as np

class KalmanFilter:
    def __init__(self, process_variance=1e-3, measurement_variance=1e-2, initial_value=0.0):
        """
        Initialize a 1D Kalman filter.

        Args:
        - process_variance (float): Variance of the process noise (Q).
        - measurement_variance (float): Variance of the measurement noise (R).
        - initial_value (float): Initial estimated state.
        """
        self.x = np.array([initial_value])           # State (filtered RSSI)
        self.P = np.array([[1.0]])                   # Estimation uncertainty (covariance)
        self.Q = np.array([[process_variance]])      # Process noise covariance
        self.R = np.array([[measurement_variance]])  # Measurement noise covariance

    def predict(self):
        """Prediction step: estimates the next state and uncertainty."""
        self.P += self.Q  # Covariance grows with process noise

    def update(self, measurement):
        """
        Update step: refines the estimate with a new measurement.
        
        Args:
        - measurement (float): The new RSSI value.

        Returns:
        - filtered_value (float): The updated RSSI estimate.
        - error (float): The estimation uncertainty.
        """
        self.predict()

        # Measurement update
        y = measurement - self.x  # Measurement residual
        S = self.P + self.R       # Innovation (uncertainty)
        K = self.P / S            # Kalman gain

        # State and covariance update
        self.x += K * y
        self.P *= (1 - K)  # Update covariance

        return self.x[0], self.P[0, 0]
