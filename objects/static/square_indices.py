# TODO: maybe this should be generated on start of the app? :C
square_indices = {
        0: slice(0, 3, None), 
        1: slice(0, 3, None), 
        2: slice(0, 3, None), 
        3: slice(3, 6, None), 
        4: slice(3, 6, None), 
        5: slice(3, 6, None), 
        6: slice(6, 9, None), 
        7: slice(6, 9, None), 
        8: slice(6, 9, None),
        }

squares = [
    (slice(0, 3, None), slice(0, 3, None)),
    (slice(0, 3, None), slice(3, 6, None)),
    (slice(0, 3, None), slice(6, 9, None)),

    (slice(3, 6, None), slice(0, 3, None)),
    (slice(3, 6, None), slice(3, 6, None)),
    (slice(3, 6, None), slice(6, 9, None)),

    (slice(6, 9, None), slice(0, 3, None)),
    (slice(6, 9, None), slice(3, 6, None)),
    (slice(6, 9, None), slice(6, 9, None)),
    ]
