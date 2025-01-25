
class Eq:
    """
    Equations class for storing useful phisics equations. Since velocity
    is constant for all objects, I won't be using derrivatives.
    """
    def t(x:float, v:float) -> float:
        """
        Calculates time with respect to distance and velocity

        Args:
            x (float): distance
            v (float): velocity
        
        Returns:
            float: time in seconds
        """
        return x / v

    def v(x:float, t:float) -> float:
        """
        Calculates velocity with respect to distance and time

        Args:
            x (float): distance
            t (float): time

        Returns:
            float: velocity in meters per second
        """
        return x / t
        
    def x(v:float, t:float) -> float:
        """
        Calculates distance with respect to time and velocity

        Args:
            v (float): velocity
            t (float): time
        
        Returns:
            float: distance in meters
        """
        return v * t