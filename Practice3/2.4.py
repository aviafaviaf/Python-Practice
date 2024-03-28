from matplotlib import pyplot as plt

PAIRS = "..LEXEGEZACEBISO" \
        "USESARMAINDIREA." \
        "ERATENBERALAVETI" \
        "EDORQUANTEISRION"


class SeedType:
    def __init__(self, w0, w1, w2):
        self.w0 = w0
        self.w1 = w1
        self.w2 = w2


class FastSeedType:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


class PlanSys:
    def __init__(
            self,
            x=0,
            y=0,
            economy=0,
            gov_type=0,
            tech_lev=0,
            population=0,
            productivity=0,
            radius=0,
            goat_soup_seed=FastSeedType(0, 0, 0, 0),
            name=""
    ):
        self.x = x
        self.y = y
        self.economy = economy
        self.gov_type = gov_type
        self.tech_lev = tech_lev
        self.population = population
        self.productivity = productivity
        self.radius = radius
        self.goat_soup_seed = goat_soup_seed
        self.name = name


def tweak_seed(s: SeedType):
    temp = s.w0 + s.w1 + s.w2
    s.w0 = s.w1
    s.w1 = s.w2
    s.w2 = temp


def make_system(s: SeedType):
    long_name_flag = s.w0 & 64

    this_sys = PlanSys()

    this_sys.x = (s.w1 >> 8) % 2 ** 32
    this_sys.y = (s.w0 >> 8) % 2 ** 32

    this_sys.gov_type = (s.w1 >> 3) & 7

    this_sys.economy = (s.w0 >> 8) & 7 if (this_sys.gov_type > 1) else this_sys.economy | 2

    this_sys.tech_lev = ((s.w1 >> 8) & 3) + (this_sys.economy ^ 7) + (this_sys.gov_type >> 1) + (
            this_sys.gov_type & 1 == 1)

    this_sys.population = 4 * this_sys.tech_lev + this_sys.economy + this_sys.gov_type + 1

    this_sys.radius = 256 * (((s.w0 >> 8) & 15) + 11) + this_sys.x

    this_sys.goat_soup_seed.a = s.w1 & 0xFF
    this_sys.goat_soup_seed.b = s.w1 >> 8
    this_sys.goat_soup_seed.c = s.w2 & 0xFF
    this_sys.goat_soup_seed.d = s.w2 >> 8

    pair1 = 2 * ((s.w2 >> 8) & 31)
    tweak_seed(s)
    pair2 = 2 * ((s.w2 >> 8) & 31)
    tweak_seed(s)
    pair3 = 2 * ((s.w2 >> 8) & 31)
    tweak_seed(s)
    pair4 = 2 * ((s.w2 >> 8) & 31)
    tweak_seed(s)

    this_sys.name = (PAIRS[pair1:pair1 + 2] + PAIRS[pair2:pair2 + 2] + PAIRS[pair3:pair3 + 2] + (
        PAIRS[pair4:pair4 + 2] if long_name_flag else "")).replace(".", "")

    return this_sys


seed = SeedType(0x5A4A, 0x0248, 0xB753)
systems = [make_system(seed) for i in range(256)]
xs, ys = zip(*((system.x, system.y) for system in systems))
names = [system.name for system in systems]

fig, ax = plt.subplots()
fig.set_size_inches(32, 16)
ax.scatter(xs, ys, color='white', s=2)
ax.set_facecolor("black")

for i, name in enumerate(names):
    ax.annotate(name, (xs[i], ys[i]), color='lightblue')

plt.show()