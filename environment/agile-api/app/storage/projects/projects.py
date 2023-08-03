from app.models.projects import Project

projects_data = [
    Project(
        id=1,
        name="ibmcloud hypersec turbo super",
        resource_ids=[1,2],
        description="has an app that hypersecurely turbo-userfriendly generates super value",
        agile_method= "scrum",
        team_members_amount=42,
        is_complete=False
    ),
Project(
        id=2,
        name="ibmcloud chatbot",
        resource_ids=[2,3],
        description="use llama 2 to query given documents based on chat input",
        agile_method= "kanban",
        team_members_amount=9,
        is_complete=True
    ),
    Project(
        id=3,
        name="ibmcloud secure storage",
        resource_ids=[3],
        description="storage provider for encrypted data at rest, in flight and ibm unable to decrypt",
        agile_method= "kanban",
        team_members_amount=4,
        is_complete=True
    ),
]


def projects():
    return projects_data
