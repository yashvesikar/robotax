class Automation(object):
    def __init__(self, productivity, cost):
        # self.annualHours = annualHours
        self.productivity = productivity
        self.cost = cost
        # self.failureRate = failureRate
    	# self.annualCost = annualCost

    def Production(self):
        return int(self.productivity)
    def Cost(self):
        return int(self.cost)
