import matplotlib.pyplot as plt
axis_font = {'size': '16'}

def plot_it(*args, subs=1, subcols=1, fg_sz=(10, 5), **kwargs):
    fsw, fsh = fg_sz
    plt.figure(figsize=(fsw, fsh*subs))

    for i in range(1, subs+1):
        plt.subplot(subs, subcols, i)
        plt.title('{}'.format(kwargs['t{}'.format(i)]), **axis_font)
        for j in range(len(args[i-1])):
            try:
                kwargs['f{}'.format(i)](*args[i-1][j], **kwargs['kw{}{}'.format(i, j+1)])
            except:
                kwargs['f{}'.format(i)](*args[i-1][j])
        if 'x{}'.format(i) in kwargs:
			plt.xlabel('{}'.format(kwargs['x{}'.format(i)]), **axis_font)
        if 'y{}'.format(i) in kwargs:
			plt.ylabel('{}'.format(kwargs['y{}'.format(i)]), **axis_font)
        if 'xlim{}'.format(i) in kwargs:
            plt.xlim(kwargs['xlim{}'.format(i)])
        if 'ylim{}'.format(i) in kwargs:
            plt.ylim(kwargs['ylim{}'.format(i)])

    plt.show()
