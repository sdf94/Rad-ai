def compress_summary(summary:str) -> str:
    """
    Compresses a summary string by replacing consecutive repeating characters with a single character followed
    by the number of repetitions.

    Args:
        summary (str): The original summary string to compress.

    Returns:
        str: The compressed summary string.

    Example:
        >>> compress_summary("This committee meets annually to assess the effectiveness of policies on environmental protection.")
        'This com2it2e2 me2ts an2ual2y to as2es2 the ef2ectivenes2 of policies on environmental protection.'
    """
    compressed_summary = ""
    prev_char = summary[0]
    char_count = 1
    
    for char in summary[1:]:
        if char == prev_char:
            char_count += 1
        else:
            if char_count == 1:
                compressed_summary += prev_char
            else:
                compressed_summary += prev_char + str(char_count)
            prev_char = char
            char_count = 1
    
    if char_count == 1:
        compressed_summary += prev_char
    else:
        compressed_summary += prev_char + str(char_count)
    
    return compressed_summary
