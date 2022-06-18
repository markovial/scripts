import pandas as pd # Pandas = panel data
import numpy as np
import os
import time

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

# print(df.shape) # tuple (rows, cols)
# print(len(df)) # num rows
# print(df.size) # rows * cols


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

# DataFrames : Merging Data / Joins {{{

# Inner join = Intersection
# Outer join = Union
# Left join  = Intersection + All in left
# Right join = Intersection + All in right

df2 = df1 = df # lines so that the following do not throw errors

pd.merge(df1 , df2 , how="inner" , left_index = True , right_index=True) # intersection              , left = df1 , right = df2 , index match
pd.merge(df1 , df2 , how="outer" , left_index = True , right_index=True) # union                     , left = df1 , right = df2 , index match
pd.merge(df1 , df2 , how="left"  , on = [ 'model' , 'year' ])            # Join on given column
pd.merge(df1 , df2 , how="right" , on = [ 'model' , 'year' ])            # Join on given column
pd.concat([df1,df2])

# }}} DataFrames : Merging Data

# DataFrames : Groups {{{

# for group , frame in df.groupby("manufacturer"): print(group)
# for group , frame in df.groupby("manufacturer"): print(frame)


cols = [ "displ","year","cty" ]

C = df.groupby("year");       # print(C)
C = df[cols].groupby("year"); # print(C)


# aggregate() : use when you have specific things you want to run for different columns , or multiple things on same col
#             : return a single row for every unique entry
# transform() : apply function to df
#             : input df
#             : return same shaped df
# filter()    : apply a function to each group dataframe ,
#             : returns True or False

# apply() : apply a function to series = an axis of df

# apply     : function elementwise     , return same shape
# transform : function whole dataframe , fill in values by row values , return same shape
# aggregate : function rows            , aggreagate condenses rows    , return new frame of aggregated unique rows


def my_func(x): return x+1

C = df["year"].aggregate ( my_func         , axis = 0 ) ; # print ( C )
C = df["year"].transform ( my_func         , axis = 0 ) ; # print ( C )
C = df["year"].transform ( lambda x: x + 1 , axis = 0 ) ; # print ( C )


C = df.groupby("year").filter( lambda x: np.nanmean(x["year"]) > 2000 ); # print(C)

# Get group , apply function to each member in group
# C = df.groupby("year").apply( my_func );

# apply function to evey element
# axis = 0 : apply function to each column
# axis = 1 : apply function to each row
C = df.apply( np.sum , axis=0 , args=() );              # print (C) 
C = df.apply( lambda x: np.max(df.columns) , axis = 0 ) # print(C)

# }}} DataFrames : Groups

# DataFrames : Pivot Tables {{{

# pivot_table()
# stack()
# unstack()


# }}} DataFrames : Pivot Tables

# DataFrames : Timestamps {{{

C = pd.Timestamp(time.ctime());                               # print (C) # Automatically set time
C = pd.Timestamp(2022,6,16,0,0);                              # print (C) # Manually set time
C = pd.Timestamp(time.ctime()).weekday();                     # print (C) # Which day of the week is it ?
C = pd.Timestamp(time.ctime()) - pd.Timestamp(2022,6,16,0,0); # print (C) # Difference between times
C = pd.Timestamp(time.ctime()) + pd.Timedelta("1D 3H");       # print (C) # Add time
C = pd.Timestamp(time.ctime()) + pd.offsets.Week();           # print (C) # Add one week
C = pd.Timestamp(time.ctime()) + pd.offsets.MonthEnd();       # print (C) # Add to months end

# Can also do crazy stuff like business day , quarterly , etc ...



C = pd.to_datetime(df["year"],dayfirst=True) # Automatically standardize various time formats for given column
                                             # dayfirst = True  : normal style
                                             # dayfirst = False : american style
                                             # nonstandard e.gs : 1/1/20 , 1.1.20 , 1-1-20 , 1 Jan 20 , Jan 1, 20 , etc ...


# }}} DataFrames : Timestamps

# BASE IMPORT {{{

# Def : clean_labels {{{


def clean_labels(df):
    """TODO: Cleans up dataframe column names
        - remove trailing spaces
        - make all values lowercase

    :df : data frame object
    :returns: DataFrame object with cleaned column values

    """

    df = df.rename(mapper = str.strip          , axis = 1) ; # Column Labels : Remove trailing whitespace
    df = df.rename(mapper = lambda x:x.lower() , axis = 1) ; # Column Labels : Change all to uppercase

    return df


# }}}

# Def : get_data {{{


def df_read_relative(path):
    """TODO: Reads in file from relative path to current file as pandas dataframe

    path : string           , relative path to file
    returns  : pandas dataframe , created from file data

    """
    dir_name  = os.path.dirname  ( __file__       )
    file_name = os.path.join     ( dir_name, path )
    file_type = os.path.splitext ( file_name      ) [1][1:]

    if   ( file_type == "csv"  ) : df = pd.read_csv     ( file_name )
    elif ( file_type == "txt"  ) : df = pd.read_csv     ( file_name )
    elif ( file_type == "zip"  ) : df = pd.read_csv     ( file_name )
    elif ( file_type == "xlsx" ) : df = pd.read_excel   ( file_name )
    elif ( file_type == "json" ) : df = pd.read_json    ( file_name )
    elif ( file_type == "html" ) : df = pd.read_html    ( file_name )
    elif ( file_type == "pdf"  ) : df = tabula.read_pdf ( file_name )
    else :
        print("dont pass in garbage filetypes")

    return df


# }}}

# if __name__ == '__main__':
    # df = df_read_relative('../data/cwurData.csv')
    # df = clean_labels(df)


# }}} BASE IMPORT




