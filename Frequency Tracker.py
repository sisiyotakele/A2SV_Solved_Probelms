class FrequencyTracker:

    def __init__(self):
        self.freq_tracker={}
        self.freq_counter={}

    def add(self, number: int) -> None:
        old = self.freq_tracker.get(number , 0)

        if old > 0:
            self.freq_counter[old] -= 1
        new = old + 1
        self.freq_tracker[number]  = new
        self.freq_counter[new] = self.freq_counter.get(new , 0) + 1



    def deleteOne(self, number: int) -> None:
        if number not in  self.freq_tracker :
            return
        old = self.freq_tracker[number]
        self.freq_counter[old] -= 1

        if old == 1:
            del self.freq_tracker[number]
        else:
            new = old - 1
            self.freq_tracker[number] = new
            self.freq_counter[new] = self.freq_counter.get(new , 0) + 1


            # self.freq_tracker[number ] -= 1
            # self.freq_counter[number ] -= 1
            # if self.freq_tracker[number] == 0:
            #     del self.freq_tracker[number]

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_counter.get(frequency,0) > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
