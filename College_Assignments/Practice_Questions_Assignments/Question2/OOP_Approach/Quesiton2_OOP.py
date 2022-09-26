class Equations:

    def __init__(self, origninal_equation):
        self.original_equation = origninal_equation
        self.normalised_equation = []
        self.degree = 0
        self.final_lis_after_phase1 = []

    def calculate_degree_of_eqn(self):
        self.degree = self.original_equation[0][1]

    def normalizing_the_eqn_phase1(self):
        deg_counter = self.degree

        for item in self.original_equation:
            if item[1] == deg_counter:
                self.final_lis_after_phase1.append([item[0], deg_counter])
                deg_counter -= 1
                continue
            else:

                while deg_counter > item[1]:
                    self.final_lis_after_phase1.append([0, deg_counter])
                    deg_counter -= 1

                self.final_lis_after_phase1.append([item[0], deg_counter])

    def normalizing_the_eqn_phase2(self, max_degree_out_of_all_equations):
        length_of_original_equation = len(self.original_equation)
        length_of_highest_order_equation = max_degree_out_of_all_equations + 1
        difference = length_of_highest_order_equation - length_of_original_equation
        counter = 1
        self.normalised_equation = self.final_lis_after_phase1

        while difference > 0:
            self.normalised_equation.insert(0, [0, (self.degree + counter)])
            difference -= 1
            counter += 1
