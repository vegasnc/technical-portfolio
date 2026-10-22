clear all
set more off
import delimited "synthetic_practice_data.csv", clear

describe
summarize hours outcome_score
tabulate group
by group, sort: summarize outcome_score

regress outcome_score hours
encode group, generate(group_id)
regress outcome_score c.hours i.group_id

twoway (scatter outcome_score hours) (lfit outcome_score hours), ///
    title("Synthetic practice data") ///
    xtitle("Hours") ytitle("Outcome score")
