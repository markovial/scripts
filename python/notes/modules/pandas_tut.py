import pandas as pd # Pandas = panel data
import numpy as np
import os

# -------------------------------------------------------
# SERIES : List of datapoints , containing : Data , Index
# -------------------------------------------------------

my_dict = { 'A' : '1', 'B' : '2', 'C' : '3', 'D' : '4', 'E':'5'}
s = pd.Series(my_dict)                                              ; # print(s) # Series : From dict
s = pd.Series( np.random.randint(0,100,5) )                         ; # print(s) # Series : auto data , auto index
s = pd.Series( np.random.randn(5) , index = ["A","B","C","D","E"] ) ; # print(s) # Series : auto data , manual index
s = pd.Series( [1,2,3,4,5] , index = ["A","B","C","D","E"] )        ; # print(s) # Series : manual data , maual index

# print(s)                                #
# print( s.append(s2) )                   # Append series to another
# print( s.head() )                       #
# print(s[0])                             # Element by index
# print( s.iloc[0] )                      # Element by index
# print(s[:1])                            # Element slice
# print(s[[4,0]])                         # Element unordered
# print(s.values)                         # Element values as list
# print( s.loc["A"] )                     # Element by key
# print(s["E"])                           # Element by key
# print(s[[True,False,False,False,True]]) # Element by boolean
# print(s > 0)                            # Element conditionals

# x = s + 1 ; print(x)
# x = s * 10 ; print(x)

# Iteration and data access
# for label,data in s.iteritems(): s.loc[label] = data*10
# for label,data in s.iteritems(): s._set_value(label,data+1)


# --------------------------------------
# DATA-FRAME : A multi dim series object
# --------------------------------------

# Dataframes : CRUD {{{

list_of_dicts = [
                    {"X":1, "Y":2 , "Z":3} ,
                    {"X":4, "Y":5 , "Z":6} ,
                    {"X":7, "Y":8 , "Z":9} ,
                ]
s1 = pd.Series( np.random.randint(0,100,5) , index = ["A","B","C","D","E"] );
s2 = pd.Series( np.random.randn(5)         , index = ["A","B","C","D","E"] );
s3 = pd.Series( [1,2,3,4,5]                , index = ["A","B","C","D","E"] );

df = pd.DataFrame([ s1,s2,s3 ]  , index=["id_1","id_2","id_3"]) ; # print(df) # DataFrame : From series
df = pd.DataFrame(list_of_dicts , index=["id_1","id_2","id_3"]) ; # print(df) # DataFrame : From list of dicts

# print( df.head() )
# df["F"] = None                                ; print(df) # Insert Column
# del(df["F"])                                  ; print(df) # Delete Column
# df.drop( "id_3" , inplace=True )              ; print(df) # Delete row
# df.drop( "X"    , inplace=True , axis=1 )     ; print(df) # Delete Column
# df.drop(['id_2' ,'id_3' ] , inplace=True)     ; print(df) # Delete row list
# df.drop( ["X","Y"] , inplace=True , axis = 1) ; print(df) # Delete column list

# }}} Dataframes : CRUD

# DataFrames : Slicing {{{

# print( df.iloc[0] )          # Row by index
# print( df["A"] )             # Column by label
# print( df.loc["id_1"] )      # Row by label
# print( df.loc["id_1"]["A"] ) # Individual Cells
# print( df.loc[:,["A","B"]] ) # Individual Cells , Slicing
# print( df.loc[:,:] )         # Individual Cells , Slicing

# cols_to_keep = ["A","B"];
# print( df[cols_to_keep] )

# }}} DataFrames : Slicing

# DataFrames : Types {{{

# print( type(df) )                  # Type
# print( type(df["A"]) )             # Type
# print( type(df.loc["id_1"]) )      # Type
# print( type(df.iloc[0]) )          # Type
# print( type(df.loc["id_1"]["A"]) ) # Type

# }}} DataFrames : Types

# DataFrames : Masks / Parsing / Conditionals {{{

print(df.shape) # tuple (rows, cols)
print(len(df)) # num rows
print(df.size) # rows * cols


# print( df          > 5 )                     # Boolean Mask
# print ((df["Y"] > 4 ) & (df["Z"] > 6))       # Boolean Mask mulitple conditions
# print ( df[ (df["Y"] > 4) & (df["Z"] > 6) ]) # Apply Mask , return values
# print ( df[ df["Y"].gt(4) & df["Z"].gt(6) ]) # Apply Mask , return values
# print ( df[ df["Y"].isin(range(1,3))] )      # Apply Mask , return values



# print( df.where(df > 5 ) )               # Apply mask , table , no drop
# print( df.where(df > 5 ).dropna() )      # Apply mask , table , drop
# print( df.where(df["Z"] > 5 ) )          # Apply mask , row   , no drop
# print( df.where(df["Z"] > 5 ).dropna() ) # Apply mask , row   , drop

# print( df[ df > 5 ] )                    # Apply mask , table , drop(?)    , inline
# print( df[ df["Z"] > 5 ] )               # Apply mask , row   , drop    , inline



# df["A"].unique() # Show only unique values


# }}} DataFrames : Masks

# DataFrames : Operations {{{


# df.sum(axis=1) # Sum of row over all columns
# df[ ['col1', 'col4', 'col5'] ].sum(axis=1) # Sum of row values in specific columns


# }}} DataFrames : Operations

# DataFrames : Read from file {{{

dirname  = os.path.dirname(__file__)
filename = os.path.join(dirname, '../data/mpg.csv')
df       = pd.read_csv(filename)
# df       = pd.read_csv(filename,error_bad_lines=False) # if faulty lines are expected in dataset , just ignore them


# }}} DataFrames : Read from file

# DataFrames : Clean Data {{{

# df = df.rename(mapper = str.strip , axis         = 'columns') ; # print(df.columns) # Column Labels : Remove trailing whitespace
# df = df.rename(mapper = lambda x:x.upper(),axis  = 1)         ; # print(df.columns) # Column Labels : Change all to uppercase
# df = df.rename(mapper = lambda x:x.upper(), axis = 'columns') ; # print(df.columns) # Column Labels : Change all to uppercase
# df.rename(mapper = lambda x:x.upper(),axis=1, inplace=True)   ; # print(df.columns) # Column Labels : Change all to uppercase
# df.columns = [x.lower() for x in df.columns ]                 ; # print(df.columns) # Column Labels : Change all to lowercase
# df.columns = [x.lower().strip() for x in df.columns ]         ; # print(df.columns) # Column Labels : Multiple Ops

# Index = row label = axis 0

# Autogen index = numeric
# Specified index = using dict , load csv specify column

# df = pd.read_csv(filename , index_col = 1) ; print(df)
# df = df.set_index("year")                  ; print(df) # overwrites current index
# df = df.sort_index()                       ; print(df) # Sort by current index
# df = df.reset_index()                      ; print(df) # resets index to default

# df.dropna()                               ; print(df) # Drop all missing (None , NaN) values
# df.fillna(0, inplace=True)                ; print(df) # Fill all missing (None) values with 0

# print ( df.replace( 1, 100 ) )                              # Replace explicit value , 1 = 100
# print ( df.replace( [1,3], [100,300] ) )                    # Replace explicit value list , 1 = 100 , 3=300
# print ( df.replace(to_replace="1", value="!" , regex=True)) # Replace by regex , NOT WORKING
# print ( df["manufacturer"].str.extract("([\w]{2})"))        # Replace data in column with matched regex
# print ( pd.to_datetime(df["year"]))                         # Replace dates with inbuilt format


# df.apply() # I dont know how this works



# }}} DataFrames : Clean Data

# DataFrames : Merging Data {{{

# Inner join = Intersection
# Outer join =  Union
# Left join
# Right join

df2 = df1 = df # lines so that the following do not throw errors
# print(df.columns)
pd.merge(df1 , df2 , how="inner" , left_index = True , right_index=True) # intersection , left = df1 , right = df2 , index match
pd.merge(df1 , df2 , how="outer" , left_index = True , right_index=True) # union        , left = df1 , right = df2 , index match
pd.merge(df1 , df2 , how="right" , on=[ 'model' , 'year' ])                            # Join on given column
pd.concat([df1,df2])

# }}} DataFrames : Merging Data

# apply function to evey element
C = df.apply( np.sum , axis=0 , args=() ); # print (C)
C = df.apply( lambda x: np.max(df.columns) , axis = 0 ) # print(C)






