using System.Threading.Tasks;

namespace RetinopathyClassification_Blazor.Pages.RetinopathyClassification
{
    public interface IRetinopathyClassificationService
    {
        Task SetPicture(string inputId, string selectedImageId, RetinopathyClassificationPageCode foodClassificationPageCode);
    }
}
