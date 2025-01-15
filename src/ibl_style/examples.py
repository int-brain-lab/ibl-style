import numpy as np


def plot_example(axs):

    # Set the seed so we get the same output each time
    np.random.seed(30)

    # Generate data for each panel
    # Panel A: Raster plot
    trials = 100
    time = np.linspace(0, 500, 500)  # 500 ms
    spike_prob = 0.02
    raster_data = (np.random.rand(trials, len(time)) < spike_prob)
    axs['a'].imshow(raster_data, cmap='binary', aspect='auto')
    axs['a'].set_xlabel("Time (ms)")
    axs['a'].set_ylabel("Trial")

    # Panel B: PSTH
    psth = np.mean(raster_data, axis=0) * 1000 / (time[1] - time[0])
    axs['b'].plot(time, psth, color='blue')
    axs['b'].set_xlabel("Time (ms)")
    axs['b'].set_ylabel("Firing rate (spikes/s)")

    # Panel C: Tuning curve
    orientations = np.linspace(0, 180, 9)
    firing_rates = (10 + 20 * np.cos(np.deg2rad(orientations - 90)) +
                    np.random.normal(0, 2, orientations.size))
    axs['c'].plot(orientations, firing_rates, marker='o', color='green')
    axs['c'].set_xlabel("Orientation (degrees)")
    axs['c'].set_ylabel("Firing rate (spikes/s)")

    # Panel D: Spike waveform
    spike_time = np.linspace(0, 2, 50)  # 2 ms
    avg_waveform = -np.exp(-(spike_time - 1)**2 / 0.1) * (1 + 0.1 * np.random.randn(spike_time.size))
    axs['d'].plot(spike_time, avg_waveform, color='purple')
    axs['d'].fill_between(spike_time, avg_waveform - 0.1, avg_waveform + 0.1, alpha=0.3, color='purple')
    axs['d'].set_xlabel("Time (ms)")
    axs['d'].set_ylabel("Amplitude (µV)")

    # Panel E: ISI histogram
    isi = np.diff(np.where(raster_data[0, :])[0])  # Inter-spike intervals
    isi_hist, isi_bins = np.histogram(isi, bins=30)
    axs['e'].bar(isi_bins[:-1], isi_hist, width=np.diff(isi_bins), color='orange', edgecolor='black')
    axs['e'].set_xlabel("Inter-spike interval (ms)")
    axs['e'].set_ylabel("Count")

    # Panel F: Receptive field map
    x, y = np.meshgrid(np.linspace(-10, 10, 100), np.linspace(-10, 10, 100))
    rf_map = 1 * np.exp(-((x - 5)**2 + (y - 3)**2) / (2 * 1 ** 2))
    axs['f_1'].imshow(rf_map, extent=(-10, 10, -10, 10), origin='lower', cmap='viridis', aspect='auto')
    axs['f_1'].set_xlabel('X position (degrees)')
    axs['f_1'].set_ylabel('Y position (degrees)')
    axs['f_2'].plot(np.mean(rf_map, axis=1), np.arange(rf_map.shape[0]))
    axs['f_2'].set_axis_off()
