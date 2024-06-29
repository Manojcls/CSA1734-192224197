% Medical diagnosis
symptom(john, fever).
symptom(john, cough).
symptom(mary, rash).
symptom(peter, headache).

diagnosis(Patient, flu) :-
    symptom(Patient, fever),
    symptom(Patient, cough).

diagnosis(Patient, measles) :-
    symptom(Patient, rash).

diagnosis(Patient, migraine) :-
    symptom(Patient, headache).
