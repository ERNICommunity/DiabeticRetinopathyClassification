using Microsoft.AspNetCore.Components;
using Microsoft.JSInterop;
using System.Threading.Tasks;

namespace RetinopathyClassification_Blazor.Pages.RetinopathyClassification
{
    public class RetinopathyClassificationPageCode : ComponentBase
    {
        [Inject]
        protected IRetinopathyClassificationService RetinopathyClassificationService { get; set; }

        public RetinopathyClassificationResponse RetinopathyClassificationResponse;

        public string InputId = "image-file";
        public string ResultId = "result";
        public string SelectedImageId = "selected-image";

        [JSInvokable("SetResult")]
        public void SetResult(RetinopathyClassificationResponse retinopathyClassification)
        {
            this.RetinopathyClassificationResponse = retinopathyClassification;
            StateHasChanged();
        }

        public async Task SetPicture()
        {
            await this.RetinopathyClassificationService.SetPicture(InputId, SelectedImageId, this);
        }
    }
}
