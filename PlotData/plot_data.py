from pylsl import StreamInlet, resolve_streams, proc_clocksync, proc_dejitter
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
#set window
pg.setConfigOption('background', (128, 128, 128))
pg.setConfigOption('foreground', 'k')
app = pg.mkQApp("Stream plotting\n")

print("Finding all streams...\n")
streams = resolve_streams()

if(len(streams) == 0):
    print("No streams were found")
    exit(0)

print("Choose stream to plot\n")
i = 1

for stream in streams:
    print(i, stream.name(), stream.uid(), stream.type())
    i += 1


x = int(input())
stream = StreamInlet(streams[x-1], processing_flags=proc_clocksync | proc_dejitter)
channel_count = stream.channel_count

pw = pg.plot(title = "Plot example")
plt = pw.getPlotItem()
plt.enableAutoRange(x=True, y=True)

empty = np.array([])
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
curves = [pg.PlotCurveItem(x=empty, y=empty, autoDownsample = True, pen = pg.mkPen(colors[i % channel_count], width = 2)) for i in range(channel_count)]

for curve in curves:
    plt.addItem(curve)



def plot():
    new_data, ts = stream.pull_chunk(0.0, 5)
    if(ts):
        print(ts,new_data)
        for i in range(channel_count):
            x_data, y_data = curves[i].getData()
            x_data = np.append(x_data, ts)
            for j in range(len(ts)):
                y_data = np.append(y_data, new_data[j][i])

            np.delete(y_data, range(len(y_data)))
            curves[i].setData(x_data, y_data)

timer = QtCore.QTimer()
timer.timeout.connect(plot)
timer.start(60)

QtGui.QGuiApplication.instance().exec()
