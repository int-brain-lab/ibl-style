import seaborn as sns
import matplotlib


def figure_style():
    sns.set(style="ticks", context="paper",
            rc={"font.size": 7,
                "axes.titlesize": 8,
                "axes.labelsize": 7,
                "axes.linewidth": 0.5,
                "axes.spines.top": False,
                "axes.spines.right": False,
                "legend.title_fontsize": 7,
                "lines.linewidth": 1,
                "lines.markersize": 4,
                "xtick.labelsize": 6,
                "ytick.labelsize": 6,
                "savefig.transparent": False,
                "xtick.major.size": 2.5,
                "ytick.major.size": 2.5,
                "xtick.major.width": 0.5,
                "ytick.major.width": 0.5,
                "xtick.minor.size": 2,
                "ytick.minor.size": 2,
                "xtick.minor.width": 0.5,
                "ytick.minor.width": 0.5,
                })
    matplotlib.rcParams['pdf.fonttype'] = 42
    matplotlib.rcParams['ps.fonttype'] = 42


def get_institute_colors():
    institutes = ['Berkeley', 'CCU', 'CSHL (C)', 'CSHL (Z)', 'NYU', 'Princeton',
                  'SWC', 'UCL', 'UCLA', 'UW', 'UCL (H)']
    colors = sns.color_palette('tab10') + [(0, 0, 0)]

    institute_colors = dict()
    for i, inst in enumerate(institutes):
        institute_colors[inst] = colors[i]

    return institute_colors


def get_lab_colors():
    lab_institute_map = {'cortexlab': 'UCL', 'mainenlab': 'CCU', 'zadorlab': 'CSHL (Z)',
                         'churchlandlab': 'CSHL (C)', 'angelakilab': 'NYU',
                         'wittenlab': 'Princeton', 'hoferlab': 'SWC', 'mrsicflogellab': 'SWC',
                         'danlab': 'Berkeley', 'steinmetzlab': 'UW', 'churchlandlab_ucla': 'UCLA',
                         'hausserlab': 'UCL (H)'}
    inst_colors = get_institute_colors()
    lab_colors = {}
    for lab, inst in lab_institute_map.items():
        lab_colors[lab] = inst_colors[inst]

    return lab_colors


def get_lab_number():
    lab_number_map = {'cortexlab': 'Lab 1', 'mainenlab': 'Lab 2', 'churchlandlab': 'Lab 3',
                      'angelakilab': 'Lab 4', 'wittenlab': 'Lab 5', 'hoferlab': 'Lab 6',
                      'mrsicflogellab': 'Lab 6', 'danlab': 'Lab 7', 'zadorlab': 'Lab 8',
                      'steinmetzlab': 'Lab 9', 'churchlandlab_ucla': 'Lab 10',
                      'hausserlab': 'Lab 11'}
    return lab_number_map
