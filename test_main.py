from main import stats, mean, median, std 
import polars as pl
df = pl.read_csv('bmi.csv')
def test_main():
    # Calculate statistics once and store them in variables
    #calculated_stats = stats(df)
    age_mean = df['Age'].mean()
    height_median = df['Height'].median()
    weight_std = df['Weight'].std()

    # Use assertions to compare specific values or properties
    #assert (stats(df) == stats(df)).all().all()
    assert (age_mean == mean(df['Age']))
    assert (height_median == median(df['Height']))
    assert (weight_std == std(df['Weight']))



if __name__ == "__main__":
  test_main()
