from enum import Enum


class UserRole(Enum):
    complainer ="complainer"
    approval = "approval"
    admin = "admin"

class ComplaintState(Enum):
    pending = "Pending"
    approved = "Approved"
    rejected = "Rejected"