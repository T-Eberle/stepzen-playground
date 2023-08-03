create table db.sustainability
(
    name                      varchar(50)  not null,
    id                        mediumint auto_increment
        primary key,
    resource_id               int          not null,
    description               varchar(250) null,
    carbon_dioxide_t          float        not null,
    particulate_matter_amount int          not null,
    power_usage_kwh           int          not null
);

INSERT INTO db.sustainability (name, id, resource_id, description, carbon_dioxide_t, particulate_matter_amount, power_usage_kwh) VALUES ('ibmcloud_vm', 1, 1, 'vm in ibm cloud', 2, 4, 12);
INSERT INTO db.sustainability (name, id, resource_id, description, carbon_dioxide_t, particulate_matter_amount, power_usage_kwh) VALUES ('ibmcloud_oc', 2, 2, 'openshift in ibm cloud', 5, 34, 532);
INSERT INTO db.sustainability (name, id, resource_id, description, carbon_dioxide_t, particulate_matter_amount, power_usage_kwh) VALUES ('ibmcloud_storage', 3, 3, 'storage in ibmcloud', 6, 3, 4);
