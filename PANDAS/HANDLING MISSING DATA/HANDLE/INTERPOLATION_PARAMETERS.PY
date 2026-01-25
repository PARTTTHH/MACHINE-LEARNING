"""
ATTRIBUTES / PARAMETERS:- THESE ARE CONTROL BEHAVIOR
1. limit:-
        HOW MANY NaNs / None ARE ALLOWED TO BE FILLED
    SYNTAX:-
        df.interpolate(method='----', limit=N)
    FILL ONLY N CONSECUTIVE MISSING VALUES, LEAVE THE REST UNTOUCHED

2. axis:-
        CONTROL DIRECTION OF INTERPOLATION OPERATION
    SYNTAX:- 
        df.interpolate(method='----', axis=0/1)
    axis=0 -> ROW-WISE [DOWN THE COLUMN]
    axis=1 -> COLUMN-WISE [ACROSS ROWS]

3. ORDER:-
        HOW COMPLEX THE CURVE LINE IS
            order = 1 → straight line
            order = 2 → smooth curve
            order = 3 → more bend

4. limit_direction :-
        THIS PARAMETER DECIDES THE DIRECTION IN WHICH THE VALID VALUES GET PROPAGATED TO FILL THE NaNs
    SYNTAX:-
        df.interpolate(method='---', limit_direction="---")

    THERE ARE THREE TYPES OF LIMIT-DIRECTION
    1. forwaed -- Fills NaNs using the last valid observation (fills "down" in a column)
    2. backward -- Fills NaNs using the next valid observation (fills "up" in a column)
    3. both --- Fills NaNs using both the previous and next valid observations

5. limit_area :-
        THIS DECIDES WHICH NaNs ARE ALLOWED TO BE FILLED
    SYNTAX:-
        df.interpolate(method='---', limit_area="---")
    THERE ARE TWO OPTIONS
    1. inside -- Fill NaNs between real values only
    2. outside -- Fill NaNs only at edges
"""

"""
interpolate()
│
├── method = HOW values are calculated = linear / time / spline / polynomial
│
├── order = how curvy the line is (for polynomial & spline)
│
├── limit = how many NaNs to fill
│
├── limit_direction = where to fill from
│
└── limit_area = which region is allowed

"""

import pandas as pd

data = {
    "A": [10, None, None, 40, None, 60]
}
df = pd.DataFrame(data)

print("ORIGINAL:")
print(df)

# limit
print("\nLIMIT = 1")
print(df.interpolate(limit=1))

# limit_direction
print("\nBACKWARD")
print(df.interpolate(limit_direction="backward"))

# limit_area
print("\nINSIDE ONLY")
print(df.interpolate(limit_area="inside"))


# ORDER
data2 = {
    "A": [10, None, 30, None, 50]
}

df2 = pd.DataFrame(data2)
print("ORIGINAL:")
print(df2)

print("\nPOLYNOMIAL order=1 (almost linear):")
print(df2.interpolate(method="polynomial", order=1))

print("\nPOLYNOMIAL order=2 (more curve):")
print(df2.interpolate(method="polynomial", order=2))
