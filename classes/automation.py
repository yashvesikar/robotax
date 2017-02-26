class Automation(object):
    def __init__(self, productivity, cost,numberOfAutomations, lifeSpan):
        # self.annualHours = annualHours
        self.productivity = productivity
        self.cost = cost
        self.lifeSpan = lifeSpan
        self.numberOfAutomations = int(numberOfAutomations)
        # self.failureRate = failureRate
    	# self.annualCost = annualCost

    def Production(self):
        return int(self.productivity)
    def Cost(self):
        return int(self.cost)
    def LifeSpan(self):
        return int(self.lifeSpan)

    def NumberOfAutomations(self):
        return self.numberOfAutomations
