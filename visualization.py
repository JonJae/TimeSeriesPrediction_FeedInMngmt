from datetime import datetime
from os.path import dirname, join
import pandas as pd
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, DataRange1d, Select
from bokeh.plotting import figure

def get_pred_dataset(src_pred, name, dataset):
    df_pred = src_pred[(src_pred.Model == name) & (src_pred.Dataset == dataset)].copy()
    del df_pred['Model']
    del df_pred['Dataset']
    df_pred['date'] = pd.to_datetime(df_pred.date)
    df_pred = df_pred.set_index(['date'])
    df_pred.sort_index(inplace=True)
    return ColumnDataSource(data=df_pred)

def get_test_dataset(src_test, name, dataset):
    df_test = src_test[(src_test.Model == name) & (src_test.Dataset == dataset)].copy()
    del df_test['Model']
    del df_test['Dataset']
    df_test['date'] = pd.to_datetime(df_test.date)
    df_test = df_test.set_index(['date'])
    df_test.sort_index(inplace=True)
    return ColumnDataSource(data=df_test)

def update_plot(attrname, old, new):
    model = model_select.value
    dataset = dataset_select.value
    step = step_select.value
    
    plot.title.text = "Predictions vs Actual Values for "+dataset+ " Set on "+step+ " calculated by "+model
    
    src_pred = get_pred_dataset(df_pred, model, dataset)
    src_test = get_test_dataset(df_test, model, dataset)

    source_pred.data.update(src_pred.data)
    source_test.data.update(src_test.data)

    line_pred.glyph.x = 'date'
    line_pred.glyph.y = step
    line_actual.glyph.x = 'date'
    line_actual.glyph.y = step
    return

model = "Naive Shift Model"
step = "Step 1"
dataset = "Validation"
title = "Predictions vs Actual Values for "+dataset+ " Set on "+step+ " calculated by "+model

model_select = Select(value=model, title='Model', options=["Naive Shift Model", "Exponential Smoothing Model", "Prophet", "Multivariate_LSTM", "Univariate_LSTM", "Multivariate_LSTM_PeepHole", "Univariate_LSTM_PeepHole"])
dataset_select = Select(value=dataset, title='Dataset', options=["Validation", "Test"])
step_select = Select(value=step, title='Step', options=["Step 1","Step 2","Step 3","Step 4","Step 5","Step 6","Step 7",
                                                        "Step 8","Step 9","Step 10","Step 11","Step 12","Step 13","Step 14",
                                                        "Step 15","Step 16","Step 17","Step 18"])

df_pred = pd.read_csv(join(dirname(__file__), './Results/predictions.csv'))
source_pred = get_pred_dataset(df_pred, model, dataset)

df_test = pd.read_csv(join(dirname(__file__), './Results/values.csv'))
source_test = get_test_dataset(df_test, model, dataset)


# changeable attributes
plot = figure(x_axis_type="datetime", plot_width=1200, tools=["box_zoom", "reset"], toolbar_location="right")
plot.title.text = title
line_pred = plot.line(x="date", y=step, source = source_pred, line_color = "blue", legend_label="Predictions")
line_actual = plot.line(x="date", y=step, source = source_test, line_color = "red", legend_label="Actual Values")

# fixed attributes
plot.xaxis.axis_label = "Time"
plot.yaxis.axis_label = "Power Loss (normed)"
plot.axis.axis_label_text_font_style = "bold"
plot.x_range = DataRange1d(range_padding=0.0)
plot.grid.grid_line_alpha = 0.3

model_select.on_change('value', update_plot)
dataset_select.on_change('value', update_plot)
step_select.on_change('value', update_plot)

controls = column(model_select, dataset_select, step_select)

curdoc().add_root(row(plot, controls))
curdoc().title = "Model Prediction vs Actual Values"