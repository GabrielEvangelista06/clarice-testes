from pydantic import BaseModel

class TextPayload(BaseModel):
    """
    Schema for the text payload.

    Attributes:
        text (str): The input text to be processed.
    """
    text: str
