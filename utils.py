# from bokeh.plotting import figure, output_file, show
# import bokeh.plotting  as bp
# from bokeh.models import HoverTool, ColumnDataSource, Div
# from bokeh.layouts import column
# import pandas as pd

# # Convert views to numeric
# def views_to_numeric(views_str):
#     views_str = views_str.replace(',', '')  # Remove commas if present
#     if 'K' in views_str:
#         views_str = views_str.replace('K', '')
#         return float(views_str) * 1000
#     elif 'M' in views_str:
#         views_str = views_str.replace('M', '')
#         return float(views_str) * 1000000
#     elif 'B' in views_str:
#         views_str = views_str.replace('B', '')
#         return float(views_str) * 1000000000
#     else:
#         return float(views_str)   

# def create_bokeh_plot(df): 
#             data = {}

#             for column in df.columns:
#                 try:
#                     print(column)
#                     data[column] = df[column]
#                 except:
#                     continue
            

#             df["Numeric Views"] = df["Views"].apply(views_to_numeric)
#             sno = list(range(1, len(df) + 1))

#             # Create a Bokeh ColumnDataSource to supply data to the plot
#             source = ColumnDataSource(df)

#             # Create a Bokeh plot
#             p = figure(
#                 title="YouTube Video Views vs. Serial Number",
#                 x_axis_label="Serial Number",
#                 y_axis_label="Views",
#                 tools="hover,pan,box_zoom,reset"
#             )

#             # Add circular markers connected by lines
#             p.line(x="index", y="Numeric Views", source=source, line_width=2, line_color="blue", legend_label="Line")
#             circle = p.circle(x="index", y="Numeric Views", source=source, size=8, color="red", alpha=0.7, legend_label="Dots")

#             # Create a custom HTML div for the hover tooltip with an image
#             hover_html = """
#                 <div>
#                     <img src="@{Thumbnail}" style="max-height: 100px;">
#                     <p><strong>Title:</strong> @{Title}</p>
#                     <p><strong>Published Time:</strong> @{Published Time}</p>
#                     <p><strong>Views:</strong> @{Views}</p>
#                 </div>
#             """

#             # Add a HoverTool with a custom tooltip
#             hover = HoverTool(renderers=[circle], tooltips=hover_html)
#             p.add_tools(hover)

#             # Add a legend
#             p.legend.title = "Legend"
            
#             p.legend.label_text_font_size = "12pt"
#             p.legend.click_policy="hide"
            
#             return p
            
 
# if __name__ == "__main__": 
#         df = pd.read_csv("scrapped_data.csv")
#         df.head()            
#         p = create_bokeh_plot(df)           

#         output_file("bokeh_plot_with_hover_and_image.html")
#         show(p)
