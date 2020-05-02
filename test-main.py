import bar_chart_race as bcr

df = bcr.load_dataset("covid19")
# print(len(df.index))
# print(df.sum(axis=1))

bar_race = bcr.bar_chart_race(
    df=df,
    filename='covid19_horiz_desc.mp4',
    orientation='h',
    sort='desc',
    label_bars=True,
    use_index=True,
    steps_per_period=10,
    period_length=500,
    figsize=(6.5, 3.5),
    cmap='dark24',
    title='COVID-19 Deaths by Country',
    bar_label_size=7,
    tick_label_size=7,
    period_label_size=16,
    fig=None)

# print(bar_race.df_values)

# bar_race.make_animation()

line_race = bcr.line_chart_race(
    series=bar_race.df_values.diff().max(axis=1),
    filename='test-line.mp4',
    line_width=3,
    use_index=True,
    steps_per_period=10,
    period_length=500,
    title="Curve",
    figsize=(6.5,3.5),
    tick_label_size=7,
    bar_label_size=7,
    period_label_size=16,
    fig=None
)

# line_race.make_animation()

# print(line_race.anim_func(1))

print(bar_race.df_values.diff().max(axis=1))

print(bar_race.get_frames())

print(line_race.get_frames())
bcr.animate_multiple_plots('multi-test.mp4',[bar_race,line_race])