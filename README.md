# Inspectorio-Test
This guide for setting up the environment on linux server.
The project require a system which uses Python 3

1. Install environment for running the project, please run "install_library.sh" in the "document" folder
2. Create an user in PostgreSQL with:
    + user_name = inspectorio_acc
    + password = inspectorio

3. Create database with shema = inspectorio
4. Create table in the above database by running the "create_table.sql" in the "document" folder
5. Grant authorization for this user with two bellow statements:
    + GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO inspectorio_acc;
    + GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO inspectorio_acc;

After finished set up environment and clone source code, we can run the project at the root of project as the following:
    + nohup python3 manage.py runserver 0.0.0.0:8000 &
And access to the website at url: http://localhost:8000/ or in the server http://149.28.23.68:8000/


 #########################################

- The diagram is organized in the "diagram_database.pdf" in the "document" folder
- There are several missing points and need to improvements which point out in the "improment.txt"
