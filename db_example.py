from sqlalchemy import create_engine, inspect, text

engine = create_engine("sqlite:////Users/elenayanushevskaya/QAP/qap21_python_project/app.db", echo=True)

insp = inspect(engine)
print(insp.get_table_names())

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM users WHERE id=6"))
    for row in result:
        print(row)

with engine.connect() as conn:
    # title           │
    # │ description     │
    # │ status          │
    # │ priority        │
    # │ board_id (FK)   │
    # │ created_by (FK) │
    # │ created_at      │
    # │ updated_at

    result = conn.execute(
        text(
            "INSERT INTO tasks (title, description, status, priority, board_id, created_by, created_at, updated_at)"
            " VALUES (:title, :description, :status, :priority, :board_id, :created_by, :created_at, :updated_at)"
        ),
        {
            "title": "1234",
            "description": "1234",
            "status": "Open",
            "priority": 1,
            "board_id": 1,
            "created_by": "34567",
            "created_at": "34567",
            "updated_at": "34567",
        },
    )
    conn.commit()
