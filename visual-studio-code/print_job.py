from queue_own import *

def add_print_job(job_id, document_name):
    job = (job_id, document_name)
    enqueue(job)

def print_job():
    if is_empty():
        print("No job in the queue")
    else:
        job = dequeue()
        print(f"printing job id:{job[0]} Document: {job[1]}")


def main():
    job_id = 1
    while True:
        print("1. Add a new job")
        print("2. Print a job")
        print("3. View total jobs")
        print("4. Exit")
        choice = input("\nSelection:")
        if choice == "1":
            while True:
                document = input("Document name:")
                if document.replace(" ", "") == "":
                    print("Document cannot be empty!!!")
                    continue
                else:
                    break
            add_print_job(job_id, document)
            job_id+=1
            print("New job successfully added")
        elif choice == "2":
            print_job()
        elif choice == "3":
            print(f"Total jobs:{get_size()}")
        elif choice == "4":
            print("Thank you for using this printer... Goodbye!")
            exit(0)
        else:
            print("Invalid menu choice!!!")


main()