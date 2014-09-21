from ..datasources import first_revision_metadata, revision_metadata
from ..util.dependencies import depends
from ..util.returns import returns


@depends(on=[first_revision_metadata, revision_metadata])
@returns(int)
def page_age_in_seconds(first_revision_metadata, revision_metadata):
    
    return revision_metadata.timestamp - first_revision_metadata.timestamp