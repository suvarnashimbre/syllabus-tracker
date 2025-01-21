from django.db.models import TextChoices


    
class DepartmentCode(TextChoices):
    CSE = "CSE", "Computer Science and Engineering"
    MECH = "MECH", "Mechanical Engineering"
    CIVIL = "CIVIL", "Civil Engineering"
    ECE = "ECE", "Electronics and Communication Engineering"
    IT = "IT", "Information Technology"
    EE = "EE", "Electrical Engineering"
    MATH = "MATH", "Mathematics"
    PHYS = "PHYS", "Physics"
    CHEM = "CHEM", "Chemistry"
    BIOTECH = "BIOTECH", "Biotechnology"
    BBA = "BBA", "Business Administration"
    COM = "COM", "Commerce"
    ENG = "ENG", "English"
    ECO = "ECO", "Economics"
    PSY = "PSY", "Psychology"


class CSEDegree(TextChoices):
    BTECH = "BTECH", "Bachelor of Technology in Computer Science"
    MTECH = "MTECH", "Master of Technology in Computer Science"
    BCA = "BCA", "Bachelor of Computer Applications"
    MCA = "MCA", "Master of Computer Applications"
    DIPLOMA = "DIPLOMA_CSE", "Diploma in Computer Science and Engineering"
    PHD = "PHD_CS", "Doctor of Philosophy in Computer Science"

class MECHDegree(TextChoices):
    BTECH = "BTECH", "Bachelor of Technology in Mechanical Engineering"
    MTECH = "MTECH", "Master of Technology in Mechanical Engineering"
    DIPLOMA = "DIPLOMA_MECH", "Diploma in Mechanical Engineering"
    PHD = "PHD_MECH", "Doctor of Philosophy in Mechanical Engineering"

class CIVILDegree(TextChoices):
    BTECH = "BTECH", "Bachelor of Technology in Civil Engineering"
    MTECH = "MTECH", "Master of Technology in Civil Engineering"
    DIPLOMA = "DIPLOMA_CIVIL", "Diploma in Civil Engineering"
    PHD = "PHD_CIVIL", "Doctor of Philosophy in Civil Engineering"
class ECEDegree(TextChoices):
    BTECH = "BTECH", "Bachelor of Technology in Electronics and Communication"
    MTECH = "MTECH", "Master of Technology in Electronics and Communication"
    DIPLOMA = "DIPLOMA_ECE", "Diploma in Electronics and Communication"
    PHD = "PHD_ECE", "Doctor of Philosophy in Electronics and Communication"
class ITDegree(TextChoices):
    BTECH = "BTECH", "Bachelor of Technology in Information Technology"
    MTECH = "MTECH", "Master of Technology in Information Technology"
    BSC_IT = "BSC_IT", "Bachelor of Science in Information Technology"
    MSC_IT = "MSC_IT", "Master of Science in Information Technology"
    DIPLOMA = "DIPLOMA_IT", "Diploma in Information Technology"
    PHD = "PHD_IT", "Doctor of Philosophy in Information Technology"
class EEDegree(TextChoices):
    BTECH = "BTECH", "Bachelor of Technology in Electrical Engineering"
    MTECH = "MTECH", "Master of Technology in Electrical Engineering"
    DIPLOMA = "DIPLOMA_EE", "Diploma in Electrical Engineering"
    PHD = "PHD_EE", "Doctor of Philosophy in Electrical Engineering"
class MATHDegree(TextChoices):
    BSC = "BSC_MATH", "Bachelor of Science in Mathematics"
    MSC = "MSC_MATH", "Master of Science in Mathematics"
    PHD = "PHD_MATH", "Doctor of Philosophy in Mathematics"
class PHYSDegree(TextChoices):
    BSC = "BSC_PHYS", "Bachelor of Science in Physics"
    MSC = "MSC_PHYS", "Master of Science in Physics"
    PHD = "PHD_PHYS", "Doctor of Philosophy in Physics"
class CHEMDegree(TextChoices):
    BSC = "BSC_CHEM", "Bachelor of Science in Chemistry"
    MSC = "MSC_CHEM", "Master of Science in Chemistry"
    PHD = "PHD_CHEM", "Doctor of Philosophy in Chemistry"
class BIOTECHDegree(TextChoices):
    BTECH = "BTECH", "Bachelor of Technology in Biotechnology"
    MTECH = "MTECH", "Master of Technology in Biotechnology"
    BSC = "BSC_BIOTECH", "Bachelor of Science in Biotechnology"
    MSC = "MSC_BIOTECH", "Master of Science in Biotechnology"
    PHD = "PHD_BIOTECH", "Doctor of Philosophy in Biotechnology"


DEGREE_CHOICES= CSEDegree.choices + MECHDegree.choices+CIVILDegree.choices+ECEDegree.choices+ITDegree.choices+EEDegree.choices+MATHDegree.choices+PHYSDegree.choices+CHEMDegree.choices+BIOTECHDegree.choices