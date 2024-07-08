## PostgreSQL

I used Docker to run the PostgreSQL, that's why there is `docker-compose.yml` file at the root.

## Backend

To setup Run the following from the `backend` folder

```bash
   pip install -r requirements.txt
```

## Frontend

To setup run the following from the `frontend` folder

```bash
    npm install
```

## How to run (dev)

1. Start the Docker container

   ```bash
       docker-compose

   ```

2. Run the migration from the backend folder, and start the server
   ```bash
        # run chmod if you cannot execute the .sh files
        scripts/migrate.sh
        scripts/start.sh
   ```
3. In a different shell run the frontend server
   ```bash
       npm run dev
   ```
   OR
   ```bash
       npm run build
       npm run preview
   ```
4. Open [localhost:5173](http://localhost:5173)
5. To see the reviews, I have added a tabular view at [localhost:5173/reviews](http://localhost:5173/reviews)

## How to run (test)

1. Start the Docker container

   ```bash
       docker-compose up
   ```

2. In the `backend folder` run
   ```bash
       pytest
   ```
