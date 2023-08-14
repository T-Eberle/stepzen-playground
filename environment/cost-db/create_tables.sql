GRANT ALL PRIVILEGES ON DATABASE cost TO "user";

create table public.cost
(
    name        varchar(50)        not null,
    resource_id integer            not null,
    description varchar(255),
    amount      varchar(20)        not null,
    type        varchar(50)        not null,
    is_paid     boolean
);

INSERT INTO cost (name, resource_id, description, amount, type, is_paid) VALUES ('ibmcloud_vm', 1, 'vm in ibm cloud', '$3.99', 'vm', true);
INSERT INTO cost (name, resource_id, description, amount, type, is_paid) VALUES ('ibmcloud_oc', 2, 'openshift in ibm cloud', '$5.99', 'cluster', false);
INSERT INTO cost (name, resource_id, description, amount, type, is_paid) VALUES ('ibmcloud_storage', 3, 'storage in ibmcloud', '$10.99', 'storage', false);

