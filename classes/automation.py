class Automation(object):
    def __init__(self, productivity, cost,numberOfAutomations, lifeSpan):
        # self.annualHours = annualHours
        self.productivity = float(productivity)
        self.cost = float(cost)
        self.lifeSpan = float(lifeSpan)
        self.numberOfAutomations = float(numberOfAutomations)
        # self.failureRate = failureRate
    	# self.annualCost = annualCost

    def Production(self):
        return self.productivity
    def Cost(self):
        return self.cost
    def LifeSpan(self):
        return self.lifeSpan

    def NumberOfAutomations(self):
        return self.numberOfAutomations
