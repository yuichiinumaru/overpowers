import math

class TemporalAdvantageHelper:
    """Helper to calculate temporal advantages in trading."""
    
    SPEED_OF_LIGHT_KMS = 299792.458  # km/s

    @staticmethod
    def calculate_light_travel_ms(distance_km):
        """Calculate one-way light travel time in milliseconds."""
        return (distance_km / TemporalAdvantageHelper.SPEED_OF_LIGHT_KMS) * 1000

    @staticmethod
    def estimate_sublinear_lead_ms(matrix_size, complexity_factor=0.001):
        """Mock estimation of sublinear lead time in milliseconds."""
        # complexity_factor represents the efficiency of the sublinear algorithm
        return math.log2(matrix_size) * complexity_factor

    def analyze_scenario(self, distance_km, matrix_size):
        light_time = self.calculate_light_travel_ms(distance_km)
        comp_lead = self.estimate_sublinear_lead_ms(matrix_size)
        advantage = light_time - comp_lead
        
        return {
            "light_travel_time_ms": light_time,
            "computational_lead_ms": comp_lead,
            "net_advantage_ms": advantage
        }

if __name__ == "__main__":
    helper = TemporalAdvantageHelper()
    
    # Tokyo to NYC scenario
    tokyo_nyc_km = 10900
    portfolio_size = 5000
    
    result = helper.analyze_scenario(tokyo_nyc_km, portfolio_size)
    print(f"--- Scenario: Tokyo to NYC ({tokyo_nyc_km} km) ---")
    print(f"Light Travel Time: {result['light_travel_time_ms']:.2f} ms")
    print(f"Estimated Comp Lead: {result['computational_lead_ms']:.2f} ms")
    print(f"Net Temporal Advantage: {result['net_advantage_ms']:.2f} ms")
