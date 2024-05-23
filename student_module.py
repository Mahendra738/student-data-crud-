import os
import json


class StudentDB:
    def __init__(self, db_json=None):
        self.db_json = db_json or "student.json"
        try:
            self.students = self.read()
            self.next_id = max(self.students.keys(), default=0) + 1
        except Exception as e:
            print(f"Error in student db: {e}")
            self.students = {}
            self.next_id = 1

    def create(self, student_obj):
        try:
            temp_id = self.next_id
            self.students[temp_id] = student_obj
            self.next_id += 1
            self.save_data()
            student_obj["id"] = temp_id  # Assign the id after success
            return {"status": "success", "id": temp_id}
        except Exception as e:
            print(f"Error in creating student: {e}")
            return {"status": "unsuccess", "error": str(e)}

    def update(self, student_obj):
        try:
            student_id = student_obj.get("id")
            if student_id in self.students:
                self.students[student_id] = student_obj
                self.save_data()
                return {"status": "success"}
            return {"status": "unsuccess", "error": "Student not available"}
        except Exception as e:
            print(f"Error in updating student: {e}")
            return {"status": "unsuccess", "error": str(e)}

    def delete(self, student_id):
        try:
            if student_id in self.students:
                del self.students[student_id]
                self.save_data()
                return {"status": "success"}
            return {"status": "unsuccess", "error": "Student not available"}
        except Exception as e:
            print(f"Error in deleting student: {e}")
            return {"status": "unsuccess", "error": str(e)}

    def read(self):
        try:
            if os.path.exists(self.db_json):
                with open(self.db_json, "r") as f:
                    students_list = json.load(f)
                    return {
                        idx: student
                        for idx, student in enumerate(students_list, start=1)
                    }
            else:
                return {}
        except Exception as e:
            print(f"Error in reading the student database: {e}")
            return {}

    def save_data(self):
        try:
            with open(self.db_json, "w") as f:
                json.dump(list(self.students.values()), f, indent=4)
        except Exception as e:
            print(f"Error in saving the student data: {e}")
