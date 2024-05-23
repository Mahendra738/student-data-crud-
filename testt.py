from student_module import StudentDB
import logging
from datetime import datetime
import os

logs_dir = 'Logs'
os.makedirs(logs_dir, exist_ok=True)

current_datetime = datetime.now()

date_string = current_datetime.strftime("%Y-%m-%d")

log_filename = os.path.join(logs_dir, f"{date_string}-data.log")

logging.basicConfig(filename=log_filename,filemode="w", level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
def main():
    
    db = StudentDB()

    logging.info("Creating students...")
    student1 = {"name": "Alpha", "age": "24", "gender": "M"}
    student2 = {"name": "bella", "age": "24", "gender": "F"}
    
    response1 = db.create(student1)
    logging.debug(response1)
    
    response2 = db.create(student2)
    logging.debug(response2)

    logging.info("\nReading students...")
    students = db.read()
    for student_id, student in students.items():
        logging.debug(f"ID: {student_id}, Student: {student}")

    logging.info("\nUpdating a student...")
    student1_updated = {"id": response1['id'], "name": "charls", "age": "22", "gender": "M"}
    update_response = db.update(student1_updated)
    logging.debug(update_response)

    logging.info("\nReading updated student...")
    updated_student = db.read().get(response1['id'])
    logging.debug(f"ID: {response1['id']}, Student: {updated_student}")

    logging.info("\nDeleting a student...")
    delete_response = db.delete(response2['id'])
    logging.debug(delete_response)

    logging.info("\nReading students after deletion...")
    students_after_deletion = db.read()
    for student_id, student in students_after_deletion.items():
        logging.debug(f"ID: {student_id}, Student: {student}")

if __name__== "__main__":
    main()