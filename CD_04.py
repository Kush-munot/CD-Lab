table = [["", "", "", "S->NP VP", "S-> NP VP", "S->NP VP",
          "S->NP VP", "S->NP VP", "S->NP VP", "S->NP VP", "S->NP VP",
          "S->NP VP", "S->NP VP", "S->NP VP",
          "S->NP VP", "S->NP VP", "S->NP VP"],
         ["", "", "", "",
          "", "", "", "NP->P",
          "NP->P", "NP->P", "NP->PN", "NP->PN",
          "NP->PN", "NP->PN", "NP->D N", "NP->D N", "NP->D N"],
         ["", "", "", "VP->V NP", "VP->V NP", "VP->V NP", "VP->V NP",
          "", "", "", "", "", "", "", "", "", ""],
         ["N->championship", "N->ball", "N->toss", "", "", "", "", "", "",
          "", "", "", "", "", "", "", ""],
         ["", "", "", "V->is", "V->want", "V->won", "V->played", "", "",
          "", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", "P->me", "P->I", "P->you", "", "",
          "", "", "", "", ""],
         ["", "", "", "", "", "", "", "", "", "", "PN->India",
          "PN->Australia", "PN->Steve", "PN->John", "", "", ""],
         ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "D->the",
          "D->a", "D->an"]
         ]


def validate(parsing_table, table_term_list, input_string, term_userdef):
    print(f"\nValidate String => {input_string}\n")
    stack = ['S', '$']
    buffer = []
    input_string = input_string.split()
    input_string.reverse()
    buffer = ['$'] + input_string
    print("{:>20} {:>20} {:>40}".format("Buffer", "Stack", "Action"))
    while True:
        # end loop if all symbols matched
        if stack == ['$'] and buffer == ['$']:
            print("{:>20} {:>20} {:>50}".format(
                ' '.join(buffer), ' '.join(stack), "Valid"))
            return "\nValid String!"
        elif stack[0] not in term_userdef:
            # take front of buffer (y) and tos (x)
            x = list(['S', 'NP', 'VP', 'N', 'V',
                     'P', 'PN', 'D']).index(stack[0])
            y = table_term_list.index(buffer[-1])
            if parsing_table[x][y] != '':
                # format table entry received
                entry = parsing_table[x][y]
                print("{:>20} {:>20} {:>50}".format(' '.join(buffer), ' '.join(
                    stack), f"T[{stack[0]}][{buffer[-1]}] = {entry}"))
                lhs_rhs = entry.split("->")
                lhs_rhs[1] = lhs_rhs[1].replace('#', '').strip()
                entryrhs = lhs_rhs[1].split()
                stack = entryrhs + stack[1:]
            else:
                return f"\nInvalid String! No rule at " \
                    f"Table[{stack[0]}][{buffer[-1]}]."
        else:
            # stack top is Terminal
            if stack[0] == buffer[-1]:
                print("{:>20} {:>20} {:>50}"
                      .format(' '.join(buffer),
                              ' '.join(stack),
                              f"Matched:{stack[0]}"))
                buffer = buffer[:-1]
                stack = stack[1:]
            else:
                return "\nInvalid String! " / "Unmatched terminal symbols"


nonterm_userdef = ['S', 'NP', 'VP', 'N', 'V', 'P', 'PN', 'D']
term_userdef = ["championship", "ball", "toss", "is", "want",
                "won", "played", "me", "I", "you", "India",
                "Australia", "Steve", "John", "the", "a", "an"]
tabTerm = ["championship", "ball", "toss", "is", "want",
           "won", "played", "me", "I", "you", "India",
           "Australia", "Steve", "John", "the", "a", "an", "$"]
sample_input_string = "India won the championship"
validity = validate(table, tabTerm, sample_input_string, term_userdef)
print(validity)
