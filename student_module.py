
# import json
# import os

# class StudentDB:
#     def _init_(self, dbjson=None):
#         self.dbjson = dbjson or "students.json"
#         if not os.path.exists(self.dbjson):
#             with open(self.dbjson, "w") as f:
#                 json.dump([], f)

#     def create(self, student_obj):
#         with open(self.dbjson, "r") as f:
#             students = json.load(f)

#         student_id = len(students) + 1
#         student_obj["id"] = student_id
#         students.append(student_obj)

#         with open(self.dbjson, "w") as f:
#             json.dump(students, f, indent=4)

#         return student_id

#     def update(self, student_obj):
#         with open(self.dbjson, "r") as f:
#             students = json.load(f)

#         for student in students:
#             if student["id"] == student_obj["id"]:
#                 student.update(student_obj)
#                 break

#         with open(self.dbjson, "w") as f:
#             json.dump(students, f, indent=4)

#     def delete(self, id):
#         with open(self.dbjson, "r") as f:
#             students = json.load(f)

#         students = [student for student in students if student["id"] != id]

#         with open(self.dbjson, "w") as f:
#             json.dump(students, f, indent=4)

#     def read(self):
#         with open(self.dbjson, "r") as f:
#             students = json.load(f)
            
#         return students

import os
import json

class StudentDB:
    def __init__(self, db_json=None):
        self.db_json = db_json or "student.json"
        try:
            self.students = self.read()
            self.next_id = max(self.students.keys(), default=0) + 1
        except Exception as e:
            print(f'Error in student db: {e}')
            self.students = {}
            self.next_id = 1


    def create(self, student_obj):
        try:
            temp_id = self.next_id
            self.students[temp_id] = student_obj
            self.next_id += 1
            self.save_data()
            student_obj['id'] = temp_id  # Assign the ID after successful insertion
            return {'status': 'success', 'id': temp_id}
        except Exception as e:
            print(f'Error in creating student: {e}')
            return {'status': 'error', 'message': str(e)}


    def update(self, student_obj):
        try:
            student_id = student_obj.get('id')
            if student_id in self.students:
                self.students[student_id] = student_obj
                self.save_data()
                return {'status': 'success'}
            return {'status': 'error', 'message': 'Student not available'}
        except Exception as e:
            print(f'Error in updating student: {e}')
            return {'status': 'error', 'message': str(e)}

    def delete(self, student_id):
        try:
            if student_id in self.students:
                del self.students[student_id]
                self.save_data()
                return {'status': 'success'}
            return {'status': 'error', 'message': 'Student not available'}
        except Exception as e:
            print(f'Error in deleting student: {e}')
            return {'status': 'error', 'message': str(e)}
        
    def read(self):
        try:
            if os.path.exists(self.db_json):
                with open(self.db_json, "r") as f:
                    students_list = json.load(f)
                    return {idx: student for idx, student in enumerate(students_list, start=1)}
            else:
                return {}
        except Exception as e:
            print(f'Error in reading the student database: {e}')
            return {}

    def save_data(self):
        try:
            with open(self.db_json, "w") as f:
                json.dump(list(self.students.values()), f, indent=4)
        except Exception as e:
            print(f'Error in saving the student data: {e}')



