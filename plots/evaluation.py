## numpy is used for creating fake data
import numpy as np
import matplotlib as mpl
## agg backend is used to create plot as a .png file
mpl.use('agg')
import matplotlib.pyplot as plt

def read_text_file(file_path):
    data =[]
    filetoread = open(file_path, 'r')
    while True:
        line = filetoread.readline()
        if not line:
            break
        data.append (float(line)*1000)
    filetoread.close()
    return data

def processdata (dir1, dir2, dir3, dir4):
    data_to_plot=[]
    data_to_plot.append(read_text_file(dir1))
    data_to_plot.append(read_text_file(dir2))
    data_to_plot.append(read_text_file(dir3))
    data_to_plot.append(read_text_file(dir4))

    return data_to_plot

def quicDelay ():
    data_to_plot = processdata("../Modbus_Quic_traffic/0ms0%/Latency.txt","../Modbus_Quic_traffic/50ms0%/Latency.txt",
                               "../Modbus_Quic_traffic/100ms0%/Latency.txt", "../Modbus_Quic_traffic/200ms0%/Latency.txt")

    # Create a figure instance
    fig = plt.figure(1, figsize=(9, 6))

    # Create an axes instance
    ax = fig.add_subplot(111)

    # Create the boxplot
    bp = ax.boxplot(data_to_plot, patch_artist=True)
    colors = ['blue', 'orange', 'green', 'red']

    ## change outline color, fill color and linewidth of the boxes
    for patch, color in zip(bp['boxes'], colors):
        # change outline color
        patch.set_facecolor(color)
        # patch.set(color='#7570b3', linewidth=2)
        # change fill color
        # box.set( facecolor = '#1b9e77' )

    ## change color and linewidth of the whiskers
    for whisker in bp['whiskers']:
        whisker.set(color='#7570b3', linewidth=2)

    ## change color and linewidth of the caps
    for cap in bp['caps']:
        cap.set(color='#7570b3', linewidth=2)

    ## change color and linewidth of the medians
    for median in bp['medians']:
        median.set(color='#b2df8a', linewidth=2)

    ## change the style of fliers and their fill
    for flier in bp['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)

    # Save the figure
    fig.savefig('fig1.png', bbox_inches='tight')

    ## Custom x-axis labels
    ax.set_xticklabels(['Sample1', 'Sample2', 'Sample3', 'Sample4'])
    ax.set_ylabel('Connection latency (ms)')
    ## Remove top axes and right axes ticks
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    fig.savefig('QUIC_delay.png', bbox_inches='tight')

def TLSDelay():

    data_to_plot = processdata("../TCP_TLS_traffic/0ms0%/Latency.txt","../TCP_TLS_traffic/50ms0%/Latency.txt",
                               "../TCP_TLS_traffic/100ms0%/Latency.txt", "../TCP_TLS_traffic/200ms0%/Latency.txt")

    # Create a figure instance
    fig = plt.figure(1, figsize=(9, 6))

    # Create an axes instance
    ax = fig.add_subplot(111)

    # Create the boxplot
    bp = ax.boxplot(data_to_plot, patch_artist=True)
    colors = ['blue', 'orange', 'green', 'red']

    ## change outline color, fill color and linewidth of the boxes
    for patch, color in zip(bp['boxes'], colors):
        # change outline color
        patch.set_facecolor(color)
        # patch.set(color='#7570b3', linewidth=2)
        # change fill color
        # box.set( facecolor = '#1b9e77' )

    ## change color and linewidth of the whiskers
    for whisker in bp['whiskers']:
        whisker.set(color='#7570b3', linewidth=2)

    ## change color and linewidth of the caps
    for cap in bp['caps']:
        cap.set(color='#7570b3', linewidth=2)

    ## change color and linewidth of the medians
    for median in bp['medians']:
        median.set(color='#b2df8a', linewidth=2)

    ## change the style of fliers and their fill
    for flier in bp['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)

    # Save the figure
    fig.savefig('fig1.png', bbox_inches='tight')

    ## Custom x-axis labels
    ax.set_xticklabels(['Sample1', 'Sample2', 'Sample3', 'Sample4'])
    ax.set_ylabel('Connection latency (ms)')
    ## Remove top axes and right axes ticks
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    fig.savefig('TLS_delay.png', bbox_inches='tight')

def quicLoss():
    data_to_plot = processdata("../Modbus_Quic_traffic/0ms0%/Latency.txt", "../Modbus_Quic_traffic/0ms10%/Latency.txt",
                               "../Modbus_Quic_traffic/0ms15%/Latency.txt", "../Modbus_Quic_traffic/0ms20%/Latency.txt")

    # Create a figure instance
    fig = plt.figure(1, figsize=(9, 6))

    # Create an axes instance
    ax = fig.add_subplot(111)

    # Create the boxplot
    bp = ax.boxplot(data_to_plot, patch_artist=True)
    colors = ['blue', 'orange', 'green', 'red']

    ## change outline color, fill color and linewidth of the boxes
    for patch, color in zip(bp['boxes'], colors):
        # change outline color
        patch.set_facecolor(color)
        # patch.set(color='#7570b3', linewidth=2)
        # change fill color
        # box.set( facecolor = '#1b9e77' )

    ## change color and linewidth of the whiskers
    for whisker in bp['whiskers']:
        whisker.set(color='#7570b3', linewidth=2)

    ## change color and linewidth of the caps
    for cap in bp['caps']:
        cap.set(color='#7570b3', linewidth=2)

    ## change color and linewidth of the medians
    for median in bp['medians']:
        median.set(color='#b2df8a', linewidth=2)

    ## change the style of fliers and their fill
    for flier in bp['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)

    # Save the figure
    fig.savefig('QUIC_loss.png', bbox_inches='tight')

    ## Custom x-axis labels
    ax.set_xticklabels(['Sample1', 'Sample2', 'Sample3', 'Sample4'])
    ax.set_ylabel('Connection latency (ms)')
    ## Remove top axes and right axes ticks
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    fig.savefig('quic_delay.png', bbox_inches='tight')

def TLSLoss():
    data_to_plot = processdata("../TCP_TLS_traffic/0ms0%/Latency.txt", "../TCP_TLS_traffic/0ms10%/Latency.txt",
                               "../TCP_TLS_traffic/0ms15%/Latency.txt", "../TCP_TLS_traffic/0ms20%/Latency.txt")

    # Create a figure instance
    fig = plt.figure(1, figsize=(9, 6))

    # Create an axes instance
    ax = fig.add_subplot(111)

    # Create the boxplot
    bp = ax.boxplot(data_to_plot, patch_artist=True)
    colors = ['blue', 'orange', 'green', 'red']

    ## change outline color, fill color and linewidth of the boxes
    for patch, color in zip(bp['boxes'], colors):
        # change outline color
        patch.set_facecolor(color)
        # patch.set(color='#7570b3', linewidth=2)
        # change fill color
        # box.set( facecolor = '#1b9e77' )

    ## change color and linewidth of the whiskers
    for whisker in bp['whiskers']:
        whisker.set(color='#7570b3', linewidth=2)

    ## change color and linewidth of the caps
    for cap in bp['caps']:
        cap.set(color='#7570b3', linewidth=2)

    ## change color and linewidth of the medians
    for median in bp['medians']:
        median.set(color='#b2df8a', linewidth=2)

    ## change the style of fliers and their fill
    for flier in bp['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)

    # Save the figure
    fig.savefig('fig1.png', bbox_inches='tight')

    ## Custom x-axis labels
    ax.set_xticklabels(['Sample1', 'Sample2', 'Sample3', 'Sample4'])
    ax.set_ylabel('Connection latency (ms)')
    ## Remove top axes and right axes ticks
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    fig.savefig('TLS_loss.png', bbox_inches='tight')


if __name__ == "__main__":
    quicDelay();
    TLSDelay();
    quicLoss();
    TLSLoss();
