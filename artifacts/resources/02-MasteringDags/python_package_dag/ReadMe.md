# Deploy DAG as ZIP file

In order to organize the DAG folder structure it is possible to deploy a dag and its components files as a ZIP package, an example of that can be found in this package, just is necessary to perform these steps

1. Go to the [python_package_dag](.)
```bash
cd artifacts/resources/02-MasteringDags/python_package_dag
```

2. Create a Zip Package
```bash
zip package_dag.zip package.py functions/*
```

3. Move the Zip Package to the dags folder
```bash
mv package_dag.zip ../dags
```