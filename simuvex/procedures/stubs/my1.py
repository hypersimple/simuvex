import simuvex

#newnew

class my1(simuvex.SimProcedure):
    def run(self):

        func_addr = self.state.regs.pc.args[0]

        # this means the return value of func xxx
        s_var = self.state.se.Unconstrained("func_" + "%x"%func_addr, self.state.arch.bits)
        
        #self.state.add_constraints(self.state.se.And(self.state.se.ULE(s_var, 126), self.state.se.UGE(s_var, 9)))
        
        return s_var
