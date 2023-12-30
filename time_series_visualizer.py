import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates = True)


# Clean data
df = df[(df["value"] < df["value"].quantile(.975)) & (df["value"] > df["value"].quantile(.025)) ]


def draw_line_plot():
    #print(df)
    # Draw line plot
    fig = plt.figure(figsize = (15,4.7))
    ax = fig.add_subplot()
    ax.plot(df.index, df["value"])
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month
    df_bar = df_bar.groupby(["year", "month"]).mean()
    df_bar = df_bar.unstack()
  
    # Draw bar plot
    fig, ax = plt.subplots(figsize = (7.5,6.6))
    df_bar.plot.bar(ax=ax, legend=True, ylabel = "Average Page Views", xlabel = "Years")
    ax.legend(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], title = "Months")
  
    #fig = df_bar.plot.bar(legend=True, ylabel = "Average Page Views", xlabel = "Years", figsize = (7.5,6.6)).figure
    #plt.legend(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], title = "Months")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    #print(df_box)
    # Draw box plots (using Seaborn)
    fig, axis = plt.subplots(1,2,figsize = (16,7))
    axis[0] = sns.boxplot(x="year", y="value", data=df_box, ax=axis[0], hue = "year", palette = sns.color_palette(n_colors = 4) ,legend=False)
    #df_box.plot.box(column = "value", by = ["year"], ax=axis[0])
    axis[0].set_title("Year-wise Box Plot (Trend)")
    axis[0].set_xlabel("Year")
    axis[0].set_ylabel("Page Views")

    axis[1] = sns.boxplot(x="month", y="value", data=df_box, ax=axis[1],  hue = "month", order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov', 'Dec'] )
    #df_box.plot.box(column = "value", by = ["month"], ax=axis[1])
    axis[1].set_title("Month-wise Box Plot (Seasonality)")
    axis[1].set_xlabel("Month")
    axis[1].set_ylabel("Page Views")



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
