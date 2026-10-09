tasks = []

def add_task(title):
    tasks.append(title)
    print(f"Task added: {title}")

def view_tasks():
    if not tasks:
        print("No tasks found.")
        return

    print("\n--- Task List ---")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def main():
    print("===== TASK TRACKER =====")

    title = input("Enter a task: ")

    add_task(title)

    view_tasks()


if __name__ == "__main__":
    main()