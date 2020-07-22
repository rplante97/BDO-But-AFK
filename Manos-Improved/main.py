from manos_clothes import manos_clothes
from manos_accessories import manos_accessories

if __name__ == "__main__":

    simulator = manos_clothes()
    #simulator = manos_accessories()
    simulator.run(base=simulator.tiers['T0'], goal=simulator.tiers['PEN'], limit=0)
    simulator.print_result(percentiles=[33, 50, 66])