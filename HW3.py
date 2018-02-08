#roblem 1:A Simple Hospital(Weight 1).
# We are interested in modeling a simple hospital where patients are admitted all
# together in the morning and are discharged all together in the evening. The hospital
# serves two types of patients: those who visit the emergency department and those who get
# hospitalized for a day. The hospital incurs $1,000 and $2,000 respectively for serving
# these patients. These costs are incurred at the time of discharge. Create a model that
#  allow you to admit patients from each type, discharge them, and returns the total operating cost
# of the hospital for this day. Hints: You will need these classes:
#
#  -Master class Patientfrom which two classes are derived: EmergencyPatientand HospitalizedPatient.
#  Patientshould have a member variable name, and an abstract method discharge()that will
# be overridden in derived classes. The discharge()method should prints the name and type of the
# patient when called.
#
#  -Class Hospitalwith variable attributes: opatientsa list to store the
# admitted patients. ocost that will get updated whenever a patient gets discharged and method
# attributes:oadmit()which admits a patient (could be of any type)odischarge_all()which calls
# the discharge()method on all patientsoget_total_cost()which returns the total operating cost of
# the hospital for this day.

# make the master class
class Patient:
    def __init__(self, name):
        self.name = name

 #add abstract method
    def discharge(self):
        raise NotImplementedError("Abstract method should be implemented in other classes.")

 #make hostpial patient class
class HospitalizedPatient(Patient):
    def __init__(self,name):
        Patient.__init__(self,name)
        self.expectedCost=2000
         #implement abstract method
    def discharge(self):
        print(self.name,'hosp patient')


 #make emergencypatient class
class EmergencyPatient(Patient):
    def __init__(self,name):
        Patient.__init__(self,name)
        self.expectedCost=1000
         #implement abstract method
    def discharge(self):
        print(self.name, 'emergency patient')


#make hospital class
class Hospital:
    def __init__(self):
        self.cost=0
        self.patient= []

    def discharge_all(self):
        for patient in self.patient:
            patient.discharge()
            self.cost += patient.expectedCost

    def admit(self, patient):
        self.patient.append(patient)

    def get_total_cost(self):
        return self.cost

#hospital
HOSP = Hospital()
#patients
Pat1 = HospitalizedPatient('1')
Pat2 = HospitalizedPatient('2')
Pat3 = EmergencyPatient('3')
Pat4 = EmergencyPatient('4')
Pat5 = EmergencyPatient('5')

HOSP.admit(Pat1)
HOSP.admit(Pat2)
HOSP.admit(Pat3)
HOSP.admit(Pat4)
HOSP.admit(Pat5)
HOSP.discharge_all()
print(HOSP.get_total_cost())


