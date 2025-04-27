
def recommend_filter(brightness_level, eye_movement_variance):
    """
    Recommend a filter based on environmental brightness and eye movement behavior.

    Args:
        brightness_level (float): Brightness level in lux.
        eye_movement_variance (float): Variance in eye movement signals.

    Returns:
        dict: Recommendation containing suggested filter and notes.
    """
    recommendation = {}

    if brightness_level > 800:
        if eye_movement_variance > 5:
            recommendation['filter'] = 'Dark Amber'
            recommendation['note'] = 'High brightness and unstable eye movement detected. Dark Amber filter recommended for maximum protection.'
        else:
            recommendation['filter'] = 'Neutral Density'
            recommendation['note'] = 'High brightness but stable eye movement. Neutral Density filter suggested.'
    elif 400 < brightness_level <= 800:
        if eye_movement_variance > 5:
            recommendation['filter'] = 'Cool Grey'
            recommendation['note'] = 'Moderate brightness with unstable eye movement. Cool Grey filter can reduce strain.'
        else:
            recommendation['filter'] = 'Light Grey'
            recommendation['note'] = 'Moderate brightness and stable eye movement. Light Grey filter sufficient.'
    else:
        recommendation['filter'] = 'No Filter Needed'
        recommendation['note'] = 'Low brightness detected. Natural vision recommended.'

    return recommendation

if __name__ == "__main__":
    # Example usage
    example = recommend_filter(brightness_level=750, eye_movement_variance=6)
    print(example)
