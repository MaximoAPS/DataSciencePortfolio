# NFL Big Data Bowl 2026 - Player Trajectory Prediction

## Project Overview

The NFL Big Data Bowl 2026 project aims to predict player trajectories in American football games using advanced machine learning techniques. The objective is to forecast future positions of players on the field based on their initial states and game context, which is crucial for understanding game dynamics, player movement patterns, and strategic decision-making.

The dataset contains comprehensive player tracking data from NFL games, including position coordinates (x, y), velocities, accelerations, player roles, and game context for each frame of gameplay. With millions of tracking records across 18 weeks of the 2023 NFL season, this project represents a significant challenge in spatiotemporal prediction.

## Data Dictionary

| Variable | Description |
|----------|-------------|
| game_id | Unique identifier for each game |
| play_id | Unique identifier for each play within a game |
| nfl_id | Unique identifier for each player |
| frame_id | Frame number within the play (0 = snap, negative = pre-snap) |
| x | Player's x-coordinate on the field (0-120 yards) |
| y | Player's y-coordinate on the field (0-53.3 yards) |
| s | Player's speed (yards per second) |
| dir | Player's direction of movement (degrees) |
| o | Player's orientation (degrees) |
| a | Player's acceleration (yards per second squared) |
| player_position | Player's position (QB, WR, CB, etc.) |
| player_role | Player's role in the play (Targeted Receiver, Defensive Coverage, etc.) |
| player_side | Player's team side (Offense/Defense) |
| player_to_predict | Boolean indicating if this player's trajectory should be predicted |
| num_frames_output | Number of frames to predict for this play |
| absolute_yardline_number | Yard line where the play starts |

## Key Findings

Through comprehensive exploratory data analysis and machine learning implementation, several critical insights were discovered:

**Data Quality Validation**: The analysis revealed exceptional data quality, with only 0.00% of records violating realistic speed constraints (>11.0 yds/s) and 0.02% violating acceleration constraints (>8.0 yds/s²). This validates the reliability of the tracking data and confirms that player movements adhere to physical constraints.

**Position-Specific Movement Patterns**: The analysis identified distinct speed distributions by player position:
- Wide Receivers (WR): Highest average speed (5.63 yds/s), reflecting their role in route running
- Cornerbacks (CB): Moderate speed (3.75 yds/s), indicating reactive defensive movements
- Quarterbacks (QB): Lowest average speed (2.03 yds/s), consistent with pocket presence

**Feature Engineering Impact**: The most significant finding was the importance of comprehensive feature engineering that captures:
- **Temporal Dynamics**: Lag features and velocity changes that model player momentum and acceleration patterns
- **Spatial Relationships**: Distances and relative velocities to nearest players, enabling understanding of player interactions
- **Game Context**: Target receiver information and field position features that provide crucial situational awareness

**Hybrid Modeling Approach**: The two-stage pipeline (endpoint prediction + trajectory correction) demonstrated superior performance compared to single-stage approaches, effectively combining initial state information with sequential trajectory patterns.

## Model Performance

The hybrid two-stage architecture achieved significant improvements:

**Stage 1 - Endpoint Predictor**:
- Predicts final positions from initial frame 0 states
- Uses CatBoost regression with MultiRMSE loss function
- Implements GroupKFold cross-validation to prevent data leakage between plays
- Automatically selects from 123 engineered features

**Stage 2 - Trajectory Corrector**:
- Refines initial MRU (uniform rectilinear motion) baseline predictions
- Learns frame-by-frame residual corrections
- Demonstrates measurable improvement over baseline predictions
- Ensures physically plausible trajectories

The multi-stage approach allows the model to leverage both snapshot information (initial state) and sequential patterns (trajectory evolution), resulting in more accurate and contextually aware predictions.

## Impact

This project provides valuable insights for multiple stakeholders in sports analytics:

- **Coaches and Analysts**: Can leverage trajectory predictions for game strategy development, player positioning analysis, and opponent scouting
- **Player Development**: Identify movement patterns, optimize training programs, and analyze player performance through data-driven insights
- **Broadcast Media**: Enhance game analysis and visualization with predictive trajectory overlays and strategic insights
- **Sports Science Researchers**: Understand player interactions, game dynamics, and movement patterns through advanced machine learning models
- **Front Offices**: Make data-driven decisions about player evaluation, scheme development, and strategic planning

The model successfully demonstrates the power of machine learning in sports analytics while highlighting the importance of domain expertise, physics-based validation, and comprehensive feature engineering in building effective predictive models for complex spatiotemporal problems.

## Technical Methodology

The solution implements a sophisticated multi-stage pipeline:

1. **Data Loading**: Parallel processing of multiple weeks of training data using ThreadPoolExecutor
2. **Feature Engineering**: Comprehensive pipeline creating 123 features across temporal, spatial, and contextual dimensions
3. **Exploratory Data Analysis**: Validation of data quality, physics constraints, and movement pattern identification
4. **Stage 1 Training**: Endpoint predictor model trained on weeks 1-12 (odd weeks)
5. **Stage 2 Training**: Trajectory corrector model trained on weeks 13-16 (even weeks)
6. **Evaluation**: Final model evaluation on test weeks 17-18

The architecture uses CatBoost gradient boosting models, which excel at handling mixed data types (numerical and categorical features) and provide robust performance on tabular data with complex feature interactions.

