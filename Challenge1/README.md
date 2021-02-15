# Challenge #1
A 3 tier environment is a common setup. Use a tool of your choosing/familiarity create these resources. Please remember we will not be judged on the outcome but more focusing on the approach, style and reproducibility.

Used - Terraform and AWS 
The public presentation tier is an nginx host serving AngularJS static content
that passes API requests through to the private application tier.

The private application tier hosts a spring boot application that persists data
in the DB tier.

The db tier hosts an RDS PostgreSQL instance.

Sample app from (here)[http://javasampleapproach.com/spring-framework/spring-mvc/angular-4-spring-jpa-postgresql-example-angular-4-http-client-spring-boot-restapi-server].

# Usage

Take a copy of terraform.tfvars.template and substitute required values.

Apply as per normal, i.e. `terraform apply -var-file=terraform.tfvars`
