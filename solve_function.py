def solve_function(unsolved_value):
    for i in range(0,365):
        COP,T_reinjection = unsolved_value[0],unsolved_value[1]

    return [
        COP/eta*T_supply-COP/eta*T_reinjection,
        COP - COP*(m_BTES*(T_BTES-T_reinjection)/m_HP(i)*(T_supply-T_return))
        ]


solved = fsolve(solve_function,[T_supply,1])
print(solved)

