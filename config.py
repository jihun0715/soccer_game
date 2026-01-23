# Centralized Configuration for Soccer Simulation

# ============================================================
# 1) Pass Logic Parameters (CalcPassDir)
# ============================================================
PASS_PARAMS = {
    # Teammate Selection
    "min_pass_threshold": 1.0,  # Minimum distance to pass
    "max_pass_threshold": 4.0,  # Maximum distance to pass
    "tm_select_w_dist": 1.0,    # Penalty weight for distance (closer is better)
    "tm_select_w_x": 1.2,       # Penalty weight for X position (forward is better)

    # Field Dimensions (Half Court for calculation)
    "field_half_length": 4.5,
    "field_half_width": 3.0,

    # Grid Search Parameters
    "max_pass_reach_x": 3.0,    # Search radius X
    "max_pass_reach_y": 2.5,    # Search radius Y
    "costmap_step": 0.2,        # Grid resolution (lower = more precise but slower)

    # Base Score Weights
    "base_score": 10.0,
    "w_abs_dx": 1.1,            # Packet dist pen X
    "w_abs_dy": 0.7,            # Packet dist pen Y
    "w_x": 0.95,                # Forward bias
    "w_y": 0.45,                # Center bias

    # Opponent Avoidance
    "receive_pass_margin": 1.15,    # Safety margin around pass path
    "opp_penalty": 24.0,        # Score penalty for blocked path
    "opp_memory_sec": 5.0,      # How long to remember opponents

    # Threshold
    "score_threshold": 6.5,     # Minimum score to attempt pass
}

# ============================================================
# 1.1) Detailed Field Dimensions (RoboCup Small Size)
# ============================================================
# All units in meters unless specified
FIELD_DIMS = {
    "length": 9.0,
    "width": 6.0,
    "line_thickness": 0.05, # 5cm
    "border_strip_min": 1.0, # Minimum 1m border
    
    # Areas
    "penalty_area_depth": 1.65,
    "penalty_area_width": 4.0,
    "goal_area_depth": 0.6,
    "goal_area_width": 2.2,
    
    # Circles & Marks
    "center_circle_diameter": 1.5, # Radius 0.75
    "penalty_mark_dist": 1.3,      # From center of goal line
    "penalty_mark_size": 0.1,      # 10cm diameter? or point? User said size is 10cm.
    
    # Goal
    "goal_width": 1.8,
    "goal_depth": 0.6, # 0.5 ~ 1.0
    "goal_height": 1.2, # Not used in 2D viz but good to have
}

# ============================================================
# 2) Striker Off-the-Ball Parameters
# ============================================================
ST_PARAMS = {
    "field_length": 9.0,
    "field_width": 6.0,
    
    # Goal/Penalty Area dims
    "penalty_dist": 1.5,
    "goal_width": 2.0,
    "circle_radius": 0.75,
    "penalty_area_length": 2.0,
    "penalty_area_width": 5.0,
    "goal_area_length": 1.0,
    "goal_area_width": 3.0,

    # Positioning Goals
    "dist_from_goal": 2.0,      # Target distance from opponent goal
    # "dist_from_goal": 3.0,    # DEFENDER

    # Weights (Cost Function)
    "base_x_weight": 6.0,#5.0       # Try to stay at 'dist_from_goal'
    "center_y_weight": 3.0,     # Try to stay central
    "defender_dist_weight": 20.0, # Avoid defenders (Weight)
    "defender_dist_cap": 3.0,   # Max distance to consider for avoidance
    
    "hysteresis_x_weight": 3.0, # Resist moving X (Stability)
    "hysteresis_y_weight": 3.0, # Resist moving Y (Stability)

    "symmetry_weight": 10.0,    # Stay symmetric to defenders?
    "ball_dist_weight": 3.0,    # Maintain specific distance from ball
    "forward_weight": 3.5,#5.2      # Biased towards opponent goal
    # "base_x_weight": 4.0,       # DEFENDER
    # "center_y_weight": 4.5,     # DEFENDER
    # "defender_dist_weight": 20.0, # DEFENDER
    # "defender_dist_cap": 3.0,   # DEFENDER
    
    # "hysteresis_x_weight": 2.5, # DEFENDER
    # "hysteresis_y_weight": 2.5, # DEFENDER

    # "symmetry_weight": 7.5,    # DEFENDER
    # "ball_dist_weight": 4.5,    # DEFENDER
    # "forward_weight": 0.5,      # DEFENDER

    # Penalties
    "penalty_weight": 10.0,     # General penalty weight
    "path_margin": 1.5,         # Margin for shot/pass paths
    "opp_memory_sec": 5.0,      

    "pass_penalty_weight": 15.0,     # Penalty if pass path blocked
    "shot_penalty_weight": 3.0,      # Penalty if shot path blocked
    "movement_penalty_weight": 30.0, # Penalty if movement path blocked
    # "penalty_weight": 10.0,     # DEFENDER
    # "path_margin": 1.5,         # DEFENDER
    # "opp_memory_sec": 5.0,      

    # "pass_penalty_weight": 15.0,     # DEFENDER
    # "shot_penalty_weight": 3.0,      # DEFENDER
    # "movement_penalty_weight": 50.0, # DEFENDER
    
    # Goal Post Avoidance
    "post_avoid_dist": 0.5,      # Distance threshold from goal post
    "post_avoid_weight": 20.0,   # Penalty weight for being too close to post

    # Search Grid
    "path_confidence": 0.5,
    "search_x_margin": 1.7,
    "grid_step": 0.1,
    # "path_confidence": 0.5, # not used
    # "search_x_margin": 2.0,   # DEFENDER
    # "grid_step": 0.1,         # DEFENDER
}

# ============================================================
# 3) Initial Game State
# ============================================================
# Coordinates: (X, Y)
# Field Range: X: [-4.5, 4.5], Y: [-3.0, 3.0]
INITIAL_POSITIONS = {
    "ball": (3.0, -2.9),
    # "ball": (-3.0, 2.5),
    "passer": (3.0, -3.0),       # Robot holding the ball
    # "passer": (-3.0, 2.6),         # Striker has the ball
    "striker": (3.0, 3.0),     # The agent we optimization
    # "striker": (0.0, 0.0),      # It's actually Defender
    "opp_user": (-1.8, 0.5),    # User controlled opponent
}

# Teammates: List of (ID, X, Y)
INITIAL_TEAMMATES = [
    # (id, x, y)
    (1, -3.5, 0.0)
]

# Opponents: List of (X, Y)
INITIAL_OPPONENTS = [
    (3.5, 0.0),
    # (0.0, 1.0)
]

# Parameters for Robot Agents
ROBOT_RADIUS = 0.35 # Used for collision/drawing

# ============================================================
# 3) Simulation Settings
# ============================================================
SIM = {
    "dt": 0.1,                 # Time step (seconds)
    "player_speed": 0.5,       # Robot speed (m/s)
    "user_step": 0.05,         # Manual control step size
}
